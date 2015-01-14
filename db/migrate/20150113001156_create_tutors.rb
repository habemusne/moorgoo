class CreateTutors < ActiveRecord::Migration
  def change
    create_table :tutors do |t|
      t.string :type
      t.string :course
      t.string :name
      t.string :phone
      t.string :email
      t.string :degree
      t.text :description

      t.timestamps
    end
  end
end
