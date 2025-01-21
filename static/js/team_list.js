$(document).ready(function() {
    // DataTable initialize
    const teamTable = $('#teamTable').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/1.10.24/i18n/Turkish.json'
        },
        order: [[0, 'asc']]
    });

    // Yeni takım ekleme
    $('#saveTeamBtn').click(function() {
        const formData = new FormData($('#addTeamForm')[0]);
        
        $.ajax({
            url: '/api/teams/',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#addTeamModal').modal('hide');
                location.reload();
            },
            error: function(xhr) {
                alert('Hata: ' + xhr.responseJSON.detail);
            }
        });
    });
});