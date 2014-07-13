class Book < ActiveRecord::Base
  belongs_to :school
  has_many :bookprices
  has_many :users, :through=> :bookprices

  before_save :to_lower_and_merge




  def to_lower_and_merge
    self.title = self.title.downcase.delete(' ')
    #self.course = self.course.downcase.delete(' ')
  end
end
