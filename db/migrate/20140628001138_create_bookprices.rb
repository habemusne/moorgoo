class CreateBookprices < ActiveRecord::Migration
  def change
    create_table :bookprices do |t|
      t.float :price
      t.integer :user_id
      t.integer :book_id
      t.string :condition
      t.text :contact

      t.timestamps
    end
  end
end
