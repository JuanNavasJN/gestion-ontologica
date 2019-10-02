const dataSet = [
    {
        id: 1,
        aspirante: 'Roberto Perez',
        fecha_test: '17/09/2019',
        evaluador: '001',
    },
    {
        id: 2,
        aspirante: 'Carlos Gonzalez',
        fecha_test: '23/09/2019',
        evaluador: '001',
    },
    {
        id: 3,
        aspirante: 'Maria Hernandez',
        fecha_test: '09/09/2019',
        evaluador: '001',
    },
    {
        id: 4,
        aspirante: 'Fiorella Infante',
        fecha_test: '09/08/2019',
        evaluador: '001',
    }
]
  
  $(document).ready(function() {
  
      var columnDefs = [{
        data: "id",
        title: "Id",
        type: "readonly"
      },
      {
        data: "aspirante",
        title: "Aspirante"
      },
     {
        data: "fecha_test",
        title: "Fecha Test"
      },
      {
        data: "evaluador",
        title: "Evaluador"
      },
      {
        data: "detalles",
        title: "Detalles",
        defaultContent: "<button class='btn btn-info'>Más Info</button>"
      }
    
    ];
        
    let myTable = $('#wartegg').DataTable({
        "sPaginationType": "full_numbers",
        data: dataSet,
        columns: columnDefs,
        dom: 'Bfrtip',        // Needs button container
        select: 'single',
        responsive: true,
        altEditor: true,     // Enable altEditor
        buttons: []
    });
     
    $('#wartegg tbody').on( 'click', 'button', function () {
        let data = myTable.row( $(this).parents('tr') ).data();
        location.replace('/dash/evaluador/wartegg/' + data.id)
    });
});
    
    