require 'google_drive'
require 'fileutils'
require 'time'
require 'yaml'

module Jekyll
  class ProgramData < Generator
    def generate(site)
      if site.config['program'] == nil
        return Jekyll.logger.warn "Conference program data not generated, because 'program' is not defined in _config.yml"
      end

      # Re-using sass-cache directory that suppose to be ignored from file watching and is cleaned with `jekyll clean`
      cacheDir = "#{site.source}/.sass-cache"
      if not File.directory? cacheDir
        FileUtils::mkdir_p cacheDir
      end

      if site.config['program']['google_client_id'] == nil
        return Jekyll.logger.warn "Conference program not generated, because 'program.google_client_id' is not defined in _config.yml"
      end

      if site.config['program']['spreadsheet'] == nil
        return Jekyll.logger.warn "Conference program not generated, because 'program.spreadsheet' is not defined in _config.yml"
      end

      begin
        session = GoogleDrive::Session.from_config(site.config['program']['google_client_id'])
        Jekyll.logger.info 'Generating conference program data from Google spreadsheets...'
        site.data['program'] = {}

        for sheetKey in site.config['program']['spreadsheet']
          begin
            Jekyll.logger.warn 'Getting data from Google Spreadsheet ', sheetKey
            spreadsheet = session.spreadsheet_by_key(sheetKey)

            for ws in spreadsheet.worksheets
              file = "#{cacheDir}/#{ws.title}.yml"
              fileMeta = "#{file}.meta"

              if File.exist?(file) and File.exist?(fileMeta)
                updated = Time.parse(File.read(fileMeta))
                if ws.updated.to_i <= updated.to_i
                  Jekyll.logger.info "Using cached version of ", file
                  site.data['program'][ws.title] = YAML.load_file(file)
                  next
                end
              end

              Jekyll.logger.warn 'Processing ', ws.title
              begin
                list = []
                ws.list.drop(1).each do |item|
                  if item['type'].empty?
                    break
                  end
                  list << item.to_hash
                end

                site.data['program'][ws.title] = list
                File.write file, list.to_yaml
                File.write fileMeta, ws.updated
              rescue
                Jekyll.logger.warn "Error processing worksheet: ", $!
              end
            end
          rescue
            Jekyll.logger.warn "Error processing spreadsheet: ", $!
          end
        end
      rescue
        # return Jekyll.logger.error "Failed to generate the conference program: ", $!
      end
    end
  end
end
