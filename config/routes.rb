Moorgoo::Application.routes.draw do
  devise_for :users
  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  root 'home#index'

  get 'video' => 'home#video'
  get 'math20b_m1_wi15' => 'home#math20b_m1_wi15'
  get 'math20b_m1_wi15_en' => 'home#math20b_m1_wi15_en'
  get 'math20b_m2_wi15' => 'home#math20b_m2_wi15'
  get 'math109_m1_1_wi15' => 'home#math109_m1_1_wi15'
  get 'math109_m1_2_wi15' => 'home#math109_m1_2_wi15'
  get 'math109_m2_wi15' => 'home#math109_m2_wi15'
  get 'math109_final_wi15' => 'home#math109_final_wi15'
  get 'econ100a_m1_wi15' => 'home#econ100a_m1_wi15'
  get 'econ100a_final_wi15' => 'home#econ100a_final_wi15'
  get 'econ120a_m2_wi15' => 'home#econ120a_m2_wi15'
  get 'econ4_final_wi15' => 'home#econ4_final_wi15'
  get 'chem6b_q1_wi15' => 'home#chem6b_q1_wi15'
  get 'chem6b_q2_wi15' => 'home#chem6b_q2_wi15'
  get 'chem6b_q4_wi15' => 'home#chem6b_q4_wi15'
  get 'chem6b_m2_wi15' => 'home#chem6b_m2_wi15'
  get 'chem6b_m3_wi15' => 'home#chem6b_m3_wi15'
  get 'chem6b_c14_wi15' => 'home#chem6b_c14_wi15'
  get 'chem6b_c15_wi15' => 'home#chem6b_c15_wi15'
  get 'chem6b_final_jsl_wi15' => 'home#chem6b_final_jsl_wi15'
  get 'chem6b_final_dave_1_wi15' => 'home#chem6b_final_dave_1_wi15'
  get 'chem140a_m1_wi15' => 'home#chem140a_m1_wi15'
  get 'chem140a_ch57_wi15' => 'home#chem140a_ch57_wi15'
  get 'chem140a_final_1_wi15' => 'home#chem140a_final_1_wi15'
  get 'phys2a_quiz1_wi15' => 'home#phys2a_quiz1_wi15'
  get 'phys2a_quiz5_wi15' => 'home#phys2a_quiz5_wi15'
  get 'phys2a_quiz6_wi15' => 'home#phys2a_quiz6_wi15'
  get 'cse11_quiz2_wi15' => 'home#cse11_quiz2_wi15'
  get 'cse11_quiz3_1_wi15' => 'home#cse11_quiz3_1_wi15'
  get 'cse11_quiz3_2_wi15' => 'home#cse11_quiz3_2_wi15'
  get 'cse11_quiz4_1_wi15' => 'home#cse11_quiz4_1_wi15'
  get 'cse11_quiz4_2_wi15' => 'home#cse11_quiz4_2_wi15'
  get 'cse11_quiz5_wi15' => 'home#cse11_quiz5_wi15'
  get 'cse11_m_wi15' => 'home#cse11_m_wi15'
  get 'cse100_m_wi15' => 'home#cse100_m_wi15'
  get 'mmw12_pp1_wi15' => 'home#mmw12_pp1_wi15'
  get 'mmw12_pp2_wi15' => 'home#mmw12_pp2_wi15'
  get 'mmw12_pp3_wi15' => 'home#mmw12_pp3_wi15'
  get 'psyc1_m1_wi15' => 'home#psyc1_m1_wi15'
  get 'psyc1_final_wi15' => 'home#psyc1_final_wi15'
  get 'mgt5_final_wi15' => 'home#mgt5_final_wi15'

  get 'math20a_m1_fa14' => 'home#math20a_m1_fa14'
  get 'math20a_m2_fa14' => 'home#math20a_m2_fa14'
  get 'math20a_final1_fa14' => 'home#math20a_final1_fa14'
  get 'math20a_final2_fa14' => 'home#math20a_final2_fa14'
  get 'math20b_final_1_wi15' => 'home#math20b_final_1_wi15'
  get 'math20b_final_2_wi15' => 'home#math20b_final_2_wi15'
  get 'math20c_m1_fa14' => 'home#math20c_m1_fa14'
  get 'math20c_m2_fa14' => 'home#math20c_m2_fa14'
  get 'math20c_final_fa14' => 'home#math20c_final_fa14'
  get 'math20e_m1_fa14' => 'home#math20e_m1_fa14'
  get 'math20e_m2_fa14' => 'home#math20e_m2_fa14'
  get 'math20e_final_fa14' => 'home#math20e_final_fa14'
  get 'math20f_m1_fa14' => 'home#math20f_m1_fa14'
  get 'math20f_m2_fa14' => 'home#math20f_m2_fa14'
  get 'math20f_final_fa14' => 'home#math20f_final_fa14'
  get 'econ1_m1_fa14' => 'home#econ1_m1_fa14'
  get 'econ1_m2_fa14' => 'home#econ1_m2_fa14'
  get 'econ1_final_fa14' => 'home#econ1_final_fa14'
  get 'econ3_m1_fa14' => 'home#econ3_m1_fa14'
  get 'econ3_m2_fa14' => 'home#econ3_m2_fa14'
  get 'econ3_final_fa14' => 'home#econ3_final_fa14'
  get 'econ4_1_fa14' => 'home#econ4_1_fa14'
  get 'econ4_2_fa14' => 'home#econ4_2_fa14'
  get 'cse11_quiz2_fa14' => 'home#cse11_quiz2_fa14'
  get 'cse11_quiz3_fa14' => 'home#cse11_quiz3_fa14'
  get 'chem6a_m2_fa14' => 'home#chem6a_m2_fa14'
  get 'chem6a_final_fa14' => 'home#chem6a_final_fa14'
  get 'sdcc_fa14' => 'home#sdcc_fa14'


  resources :tutor_requests
  resources :tutors
  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end
end
