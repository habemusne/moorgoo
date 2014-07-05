class ModifyUserTable < ActiveRecord::Migration
  def change
    remove_column :books, :user_id, :integer
    remove_column :books, :price, :float
    remove_column :books, :condition, :string
    add_column :books, :pic_url, :string
    add_column :books, :author, :string
  end
end
