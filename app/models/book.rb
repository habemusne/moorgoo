class Book < ActiveRecord::Base
  belongs_to :school
  has_many :bookprices
  has_many :users, :through=> :bookprices

  before_save :generalize_course

  def self.similar_search( type, word )
    @books = []
    p type
    if type == "title"
      result = {}
      self.all.each do |b|
        result[b.id] = word.similar b.title
      end
      result.sort_by{|k,v| v}.last(5).each do |f|
        @books << Book.find(f[0])
      end
    else
      @books = Book.where(type => word.downcase.delete(' '))
    end
    @books
  end

  def generalize_course
    self.course = self.course.downcase.delete ' '
  end

end
