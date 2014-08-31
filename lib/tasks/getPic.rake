require 'open-uri'
require 'Nokogiri'

task :getPic, [:isbn] => [:environment] do |t, args|
  puts "Args were: #{args}"
  url = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=#{:isbn}"
  img = Nokogiri::HTML(open(url)).xpath("//div[@id='result_0']/div/a/div/img")
  if img.empty?
    p "empty"
  else
    src = img.attribute("src").text()
    p src
  end
end