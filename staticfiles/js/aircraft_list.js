$(document).ready(function() {
    // DataTable initialize
    const aircraftTable = $('#aircraftTable').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/1.10.24/i18n/Turkish.json'
        },
        order: [[6, 'desc']]
    });

    // Uçak tipi seçildiğinde parçaları güncelle
    $('#aircraftType').change(function() {
        const aircraftTypeId = $(this).val();
        if (aircraftTypeId) {
            updatePartDropdowns(aircraftTypeId);
        }
    });

    function updatePartDropdowns(aircraftTypeId) {
        // Her parça tipi için ayrı AJAX çağrısı
        const partTypes = ['wing', 'body', 'tail', 'avionics'];
        
        partTypes.forEach(function(type) {
            $.get(`/api/parts/?type=${type.toUpperCase()}&aircraft_type=${aircraftTypeId}&is_used=false`, function(data) {
                const dropdown = $(`#${type}`);
                dropdown.empty().append('<option value="">Seçiniz</option>');
                
                data.forEach(function(part) {
                    dropdown.append(`<option value="${part.id}">${part.type} - ${part.created_at}</option>`);
                });
            });
        });
    }

    // Yeni uçak üretme
    $('#saveAircraftBtn').click(function() {
        const formData = new FormData($('#addAircraftForm')[0]);
        
        $.ajax({
            url: '/api/aircraft/',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#addAircraftModal').modal('hide');
                location.reload();
            },
            error: function(xhr) {
                alert('Hata: ' + xhr.responseJSON.detail);
            }
        });
    });
});