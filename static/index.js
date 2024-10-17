$(document).ready(function() {
    var $facilitySelect = $('#facilities'),
        $departmentSelect = $('#departments'),
        $options=$departmentSelect.find('option');
        
        $facilitySelect.on('change', function() {
            $departmentSelect.html($options.filter('[value="' + this.value+ '"]'));
        }).trigger('change');
});
