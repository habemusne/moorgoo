class Bookprice < ActiveRecord::Base
  belongs_to :book
  belongs_to :user

  def inverseStatus
    self.status == 0 ? 1 : 0
  end

end
