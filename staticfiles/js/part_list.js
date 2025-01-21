$(document).ready(function() {
    // DataTable initialize
    const partTable = $('#partTable').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/1.10.24/i18n/Turkish.json'
        },
        order: [[3, 'desc']]
    });

    // Yeni parça ekleme
    $('#savePartBtn').click(function() {
        const formData = new FormData($('#addPartForm')[0]);
        
        $.ajax({
            url: '/api/parts/',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#addPartModal').modal('hide');
                location.reload();
            },
            error: function(xhr) {
                alert('Hata: ' + xhr.responseJSON.detail);
            }
        });
    });

    // Parça silme
    $('.delete-part').click(function() {
        if (confirm('Bu parçayı silmek istediğinizden emin misiniz?')) {
            const partId = $(this).data('id');
            
            $.ajax({
                url: `/api/parts/${partId}/`,
                method: 'DELETE',
                success: function() {
                    location.reload();
                },
                error: function(xhr) {
                    alert('Hata: ' + xhr.responseJSON.detail);
                }
            });
        }
    });
});