// Resources
var options_resources = {
  valueNames: [ 'author', 'title', 'category', 'year', 'starred' ]
};

var resourceList = new List('table-resources', options_resources);

$(document).ready(function () {
    $('#filter-material').change(function () {
        var selection = this.value;
        if (selection) {
            resourceList.filter(function(item) {
                return (item.values().category == selection);
            });
        } else {
            userList.filter();
        }
    });
});

// Courses
var options_courses = {
  valueNames: [ 'author', 'title', 'designation', 'university', 'year', 'starred']
};

var courseList = new List('table-courses', options_courses);

// Tools
var options_tools = {
  valueNames: [ 'name', 'topic', 'description']
};

var toolList = new List('table-tools', options_tools);

// Videos
var options_videos = {
  valueNames: [ 'author', 'organization', 'name', 'description']
};

var videoList = new List('table-videos', options_videos);