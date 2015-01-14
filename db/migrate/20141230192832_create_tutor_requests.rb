class CreateTutorRequests < ActiveRecord::Migration
  def change
    create_table :tutor_requests do |t|
      t.string :school
      t.string :course
      t.string :length
      t.string :area
      t.string :time_one
      t.string :time_two
      t.string :time_three
      t.integer :user_id
      t.string :frequency
      t.boolean :paid, default: false

      t.timestamps
    end
  end
end
