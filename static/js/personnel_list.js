$(document).ready(function() {
    // DataTable initialize
    const personnelTable = $('#personnelTable').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/1.10.24/i18n/Turkish.json'
        },
        order: [[0, 'asc']]
    });

    // Yeni personel ekleme
    $('#savePersonnelBtn').click(function() {
        const formData = new FormData($('#addPersonnelForm')[0]);
        
        $.ajax({
            url: '/api/personnel/',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#addPersonnelModal').modal('hide');
                location.reload();
            },
            error: function(xhr) {
                alert('Hata: ' + xhr.responseJSON.detail);
            }
        });
    });
});