module Jekyll
  module RegexFilter
    def replace_regex(input, reg_str, repl_str)
      input.to_s.gsub(Regexp.new(reg_str), repl_str.to_s)
    end
  end
end

Liquid::Template.register_filter(Jekyll::RegexFilter)
