class Bookprice < ActiveRecord::Base
  belongs_to :book
  belongs_to :user
  scope :valid, ->{ where(["user_id > ? and status = ? ", 0, 0])}


  protected

  def inverseStatus
    self.status == 0 ? 1 : 0
  end

end
