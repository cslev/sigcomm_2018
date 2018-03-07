require 'json'
require 'csv'
require 'pandoc-ruby'

def english_join(array = nil)
  return array.join('') if array.nil? or array.length <= 1
  return array.join(" and ") if array.length == 2
  array[0..-2].join(", ") + ", and " + array[-1]
end

ARGV.each do |file|
  # print file
  papers = JSON.load File.new(file, :internal_encoding => 'utf-8', :external_encoding => 'utf-8')

  CSV.open("#{file}.csv", "w", {:force_quotes=>true,
                                :write_headers=> true,
                                :headers => ['type', 'time', 'room', 'title', 'authors', 'abstract']}) do |output|
    papers.each do |paper|
      print "#{ paper['title']}\n"

      authors = []
      lastAuthors = []
      lastAffiliation = nil

      if paper['authors'].nil? then
        print "+++++++++ #{paper['pid']} cannot be processed\n"
        next
      end

      paper['authors'].each do |author|
        if lastAffiliation != author['affiliation'] then
          if lastAuthors.length > 0 then
            authorSet = english_join(lastAuthors)
            if not lastAffiliation.nil? then
              authorSet += " (" << lastAffiliation << ")"
            end
            authors << authorSet
            lastAuthors = []
          end
        end
        lastAuthors << "#{author['first']} #{author['last']}"
        lastAffiliation = author['affiliation']
      end

      authorSet = english_join(lastAuthors)
      if not lastAffiliation.nil? then
        authorSet += " (" << lastAffiliation << ")"
      end
      authors << authorSet

      # print english_join(authors)
      # print "\n"

      begin
        if paper['abstract'].length > 0
          abstract = PandocRuby.convert(paper['abstract'], :from => :latex, :to => :html)
        end

        if abstract.length < 0.98 * paper['abstract'].length then
          print " >>> SWITCH TO PLAINTEXT ABSTRACT\n"
          abstract = PandocRuby.convert(paper['abstract'], :from => :markdown, :to => :html)
        end
      rescue
        print " >>> LaTeX error, switch to plaintext abstract\n"
        abstract = PandocRuby.convert(paper['abstract'], :from => :markdown, :to => :html)
      end

      output << ['paper',
                 '', '', paper['title'], english_join(authors),
                 "#{abstract}"]
    end
  end
end
