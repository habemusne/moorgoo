class Addstatustobookprice < ActiveRecord::Migration
  def change
    add_column :bookprices, :status, :integer, :default=>0
  end
end
