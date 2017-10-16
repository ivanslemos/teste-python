% rebase('layout.tpl', title='Home Page', year=year)
 


 <div class='box-formulario'>

		<div class='header-form'>
 		 <h2>Hoteis</h2> 
		</div>	

		 <!-- formularios -->
		 <form id="Formulario"  class="col-md-12 formulario">
				  
				  <h3>+170.000 hoteis, pousadas e resorts no mundo todo </h3>

				  <div class= "col-md-12 "  style="height: 100px;">
						  <div class="col-md-4">
							<label for="HoteisList">Quer ficar onde?</label>
							<select id="HoteisList" placeholder="Cidade ou Hotel" name="local" class="form-control idhotel" required></select>	
						  </div>


						  <div class="col-md-8">
				  					<div class="col-md-6">
										<label  >Quando?(Entrada e Saida)</label>
										<input type="text" name="data-inicio" class="form-control  data-inicio" placeholder="Entrada"  />
										<div class="form-check">
											<label class="form-check-label">
											  <input type="checkbox" class="form-check-input sem-data">
											  Ainda nao defini a data
											</label>
										</div>
									</div>
									<div class="col-md-6">
											<label  ></label>
											<input type="text" name="data-fim " class="form-control data-fim " placeholder="Saida"  />
									</div>

						  </div>

						  <div class="col-md-12 text-center"  style="    float: left;" > <button id="BtPesquisar" type="submit" class="btn btn-primary  " >Buscar</button></div>
 
						 
				  </div>
				  
				  


				  
				   
				   
				   
				   
				 
				 
		  </form>
  </div>



  <!-- loader -->
   <div class="loader  text-center   " style="display:none;">
		<img src="/static/images/ajax-loader.gif" >
   </div>




   <!-- resultado -->
  <div class="resultado-busca col-md-12 mt-10" style="display:none;">
		<h3>Resultado</h3>

		<table class="table table-hover">
				  <thead>
					<tr>
					  <th>Hotel</th>
					  <th>Cidade</th>
					  <th>Data</th>
					  <th>Vaga</th>
					  <th>Total de noites disponiveis</th>
					</tr>
				  </thead>
				  <tbody id="BoxResutado">
 
				  </tbody>
		</table>
  
  </div>


 <!-- modal de aviso -->
 
 
<!-- Modal -->
<div id="ModalAviso" class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Aviso</h5>
      
      </div>
      <div class="modal-body text-center ">
        <p> Voce nao preencheu o campo de data inicio e fim corretamente. Caso queira prosseguir sem defirnir uma data, selecione a opcao <strong>Ainda nao defini a data</strong> e tente novamente.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Fechar</button>
   
      </div>
    </div>
  </div>
</div>