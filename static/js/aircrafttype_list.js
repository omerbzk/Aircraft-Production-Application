$(document).ready(function() {
    // DataTable initialize
    const aircraftTypeTable = $('#aircraftTypeTable').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/1.10.24/i18n/Turkish.json'
        },
        order: [[0, 'asc']]
    });

    // Yeni uçak tipi ekleme
    $('#saveAircraftTypeBtn').click(function() {
        const formData = new FormData($('#addAircraftTypeForm')[0]);
        
        $.ajax({
            url: '/api/aircraft-types/',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#addAircraftTypeModal').modal('hide');
                location.reload();
            },
            error: function(xhr) {
                alert('Hata: ' + xhr.responseJSON.detail);
            }
        });
    });
});