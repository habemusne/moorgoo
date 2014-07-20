class Bookprice < ActiveRecord::Base
  belongs_to :book
  belongs_to :user
  default_scope{ where("user_id IS NOT NULL")}


  def inverseStatus
    self.status == 0 ? 1 : 0
  end

end
