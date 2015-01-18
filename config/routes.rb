Moorgoo::Application.routes.draw do
  devise_for :users
  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  root 'home#index'

  get 'video' => 'home#video'
  get 'math20a_m1_fa14' => 'home#math20a_m1_fa14'
  get 'math20a_m2_fa14' => 'home#math20a_m2_fa14'
  get 'math20a_final1_fa14' => 'home#math20a_final1_fa14'
  get 'math20a_final2_fa14' => 'home#math20a_final2_fa14'
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
