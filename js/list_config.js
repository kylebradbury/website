var options = {
  valueNames: [ 'author', 'title', 'category', 'year', 'starred' ]
};

var userList = new List('users', options);

$(document).ready(function () {
    $('#filter-material').change(function () {
        var selection = this.value;
        if (selection) {
            userList.filter(function(item) {
                return (item.values().category == selection);
            });
        } else {
            userList.filter();
        }
    });
});


var options2 = {
  valueNames: [ 'author', 'title', 'designation', 'university', 'year', 'starred']
};

var courseList = new List('classes', options2);

$(document).ready(function () {
    $('#filter-material').change(function () {
        var selection = this.value;
        if (selection) {
            courseList.filter(function(item) {
                return (item.values().category == selection);
            });
        } else {
            courseList.filter();
        }
    });
});