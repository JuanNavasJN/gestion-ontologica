const factors = [
  'B Razonamienton',
  'A Afabilidad',
  'C Estabilidad',
  'E Dominancia',
  'F Animación',  
  'G Atención normas',
  'H Atrevimiento',
  'I Sensibilidad',
  'L Vigilancia',
  'M Abstracción',
  'N Privacidad',
  'O Aprensión',
  'Q1 Apertura cambio',
  'Q2 Autosuficiencia',
  'Q3 Perfeccionismo',
  'Q4 Tensión'
]

$(document).ready(function() {

    var dataSet = [
  {id:1, question:"Lorem ipsum dolor sit amet consectetur adipisicing elit.", factor:"System Architect"},

    ];
  
    var columnDefs = [{
      data: "id",
      title: "Id",
      type: "readonly"
    },
    {
      data: "question",
      title: "Pregunta"
    },
   {
      data: "factor",
      title: "Factor"
    }];
  
    var myTable;
  
    myTable = $('#16pf').DataTable({
      "sPaginationType": "full_numbers",
      data: dataSet,
      columns: columnDefs,
      dom: 'Bfrtip',        // Needs button container
      select: 'single',
      responsive: true,
      altEditor: true,     // Enable altEditor
      buttons: [{
              text: 'Agregar',
              name: 'add'        // do not change name
            },
  
            {
              extend: 'selected', // Bind to Selected row
              text: 'Editar',
              name: 'edit'        // do not change name
            },
  
            {
              extend: 'selected', // Bind to Selected row
              text: 'Eliminar',
              name: 'delete'      // do not change name
           }]
    });
  
  
  });
  
  