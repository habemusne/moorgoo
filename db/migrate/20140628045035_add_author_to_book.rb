class AddAuthorToBook < ActiveRecord::Migration
  def change
    add_column :books, :author, :string
  end
end
