class User < ActiveRecord::Base
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable, :confirmable,
         :recoverable, :rememberable, :trackable, :validatable
  belongs_to :school
  has_many :bookprices
  has_many :books, :through=> :bookprices
  ADMIN_LIST = ["z2tao@ucsd.edu", "nac001@ucsd.edu", "sil024@ucsd.edu"]

  def admin?
    User::ADMIN_LIST.include? self.email
  end
end
