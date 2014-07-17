class Book < ActiveRecord::Base
  belongs_to :school
  has_many :bookprices
  has_many :users, :through=> :bookprices

  before_save :generalize_course

  def self.similar_search( word )
    if word.to_i == 0
      @books = Book.where(:course => word.delete(' ').downcase())
      if @books.empty?
        @books = Book.find_by_title( word )
      end
    else
      @books = Book.where(:isbn => word.to_i )
    end
    @books
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
    books
  end

  def generalize_course
    self.course = self.course.delete(' ').downcase()
  end

end
