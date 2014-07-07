# deprecated!
class Addisbntoprice < ActiveRecord::Migration
  def change
    add_column :bookprices, :isbn, :long, index: true
    change_column :books, :isbn, :long, index: true
  end
end
