require 'liquid'
require 'digest'

module Jekyll
  module FileDigest
    class Tag < Liquid::Tag
      def initialize(tag_name, file_name, tokens)
        super
        @file_name = file_name.strip
      end

      def render(context)
        Digest::SHA256.file("#{context.registers[:site].config['source']}/#{@file_name}")
      end
    end
  end
end

Liquid::Template.register_tag('file_digest', Jekyll::FileDigest::Tag)
