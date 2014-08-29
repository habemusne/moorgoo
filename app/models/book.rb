require 'open-uri'
require 'Nokogiri'
class Book < ActiveRecord::Base
  belongs_to :school
  has_many :bookprices
  has_many :users, :through=> :bookprices
  after_save :rescue_pic


  def self.similar_search( word )
    if word.to_i == 0
      @books = Book.where(:course => word.delete(' ').downcase())
      if @books.empty?
        @books = Book.find_by_title( word )
      end
    else
      @books = Book.where( :isbn => word )
    end
  end

  def self.find_by_title( title )
    result = {}
    books = []
    self.all.each do |b|
      result[b.id] = title.similar b.title
    end
    result.sort_by{|k,v| v}.last(6).each do |f|
      books << Book.find(f[0])
    end
    books.reverse
  end

  def generalize_course
    self.course = self.course.delete(' ').downcase()
  end

  def self.processISBN(isbn)
    # p "processISBN called"
    book = Book.find_by(:isbn => isbn) || Book.fetch_book(isbn)
  end

  def self.convertISBN(isbn)
    # p "convertISBN called"
    if isbn.length == 10
      isbn_13 = "978" + isbn.from(0).to(8) + ((10 - (9 + 3*7 + 8 + 3*(isbn.at(0).to_i) + isbn.at(1).to_i + 3*(isbn.at(2).to_i) + isbn.at(3).to_i + 3*(isbn.at(4).to_i) + isbn.at(5).to_i + 3*(isbn.at(6).to_i) + isbn.at(7).to_i + 3*(isbn.at(8).to_i)) % 10) % 10).to_s
    else
      isbn_13 = isbn
    end
    return isbn_13
  end

  def self.fetch_book(isbn)
    # p "fetch_book called"
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:#{isbn}"
    result = JSON.load(open(url).read)
    if result["totalItems"] == 0
      nil
    else
      begin
        book = Book.new(
          :title => result["items"][0]["volumeInfo"]["title"],
          :isbn => isbn,
          :author => result["items"][0]["volumeInfo"]["authors"][0] || " ",
          :pic_url => result["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
        )
      rescue
        nil
      end
    end
  end

  def self.create_new_book(isbn, course, title, school_id)
    if isbn != "None"
      book = processISBN(isbn)
    end
    book ||= Book.new(:isbn=>isbn, :title=>title, :school_id=>school_id)
    book.course = course
    book.save
    book
  end

  def rescue_pic
    if self.isbn.to_i > 0 && self.pic_url.nil?
      url = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=#{self.isbn}"
      img = Nokogiri::HTML(open(url)).xpath("//div[@id='result_0']/div/a/div/img")
      if img.empty?
        p "empty"
      else
        src = img.attribute("src").text()
        p src
        Book.find(self.id).update_attribute(:pic_url, src)
      end
    end
  end


end
