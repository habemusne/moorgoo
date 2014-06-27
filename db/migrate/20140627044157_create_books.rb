class CreateBooks < ActiveRecord::Migration
  def change
    create_table :books do |t|
      t.string :isbn
      t.string :title
      t.integer :user_id
      t.float :price
      t.string :course
      t.string :condition
      t.integer :school_id
      t.string :edition

      t.timestamps
    end
  end
end
