class AddConfirmationToTutorRequest < ActiveRecord::Migration
  def change
    add_column :tutor_requests, :code, :string
  end
end
