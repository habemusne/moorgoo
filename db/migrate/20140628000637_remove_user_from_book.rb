class RemoveUserFromBook < ActiveRecord::Migration
  def change
    remove_column :books, :user_id
    remove_column :books, :price
    remove_column :books, :condition
    add_column :books, :pic_url, :string
  end
end
