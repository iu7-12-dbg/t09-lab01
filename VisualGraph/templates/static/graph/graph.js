/**
 * Created by Nikita on 18.11.2015.
 */
var Constants = {
    pathColor : "#FFB942",
    graphColor : "#1AC7B2",
    graphInputRegExp: /^\s*nodes\s*:\s*([\d]+\s*\[\s*[\d]+\s*:\s*[\d]+\s*]\s*,\s*)*\s*[\d]+\s*\[\s*[\d]+\s*:\s*[\d]+\s*]\s*;\s*arcs\s*:\s*([\d]+\s*->\s*[\d]+\s*\[[\d]+]\s*,)*\s*[\d]+\s*->\s*[\d]+\s*\[\s*[\d]+\s*]\s*$/,
    maxNodeCoordinateValue: 100
};

//{"arcs": [{"a": 0, "b": 1, "w": 10},...], "nodes": [{"value": 0, "x": 10, "y":5},...]}

function onCalculateAStarButtonClicked() {
    var pk = document.getElementById("viewArea").getAttribute("pk");
    var from = document.getElementById("aStarFrom").value;
    var to = document.getElementById("aStarTo").value;

    if (!pk || !from || !to) {
        alert('PK, from or to are not specified!');
        return;
    }

    $.ajax(
        {
            url : "/graph/solve/" + pk + '/' + from + '/' + to,
            success : function(path) {
                redrawGraph(document.getElementById("viewArea").getAttribute("graphJSON"), path);
            },
            error : function() {
                alert("Error executing A Star :(");
            }
        }
    );
}

function redrawGraph(graphJSON, path) {
    var graph = typeof graphJSON == 'object' ? graphJSON : JSON.parse(graphJSON);

    if (graph == undefined) {
        var network = new vis.Network(
            document.getElementById("viewArea"),
            {}, {}
        );

        return;
    }

    if (typeof path == 'string') {
        path = JSON.parse(path);
    }

    var arcs = [];
    var nodes = [];

    for (var i = 0; i < graph.nodes.length; ++i) {
        var node = graph.nodes[i];
        nodes.push(
            {
                id: node.value,
                label : node.value + '[' + node.x + ',' + node.y + ']',
                color : (path != undefined && path.indexOf(node.value) > -1) ?
                         Constants.pathColor : Constants.graphColor
            }
        );
    }

    for (var j = 0; j < graph.arcs.length; ++j) {
        var arc = graph.arcs[j];
        arcs.push(
            {
                from : arc.a,
                label : arc.w,
                to : arc.b,
                color : isArcInPath(arc, path) ? Constants.pathColor : Constants.graphColor
            }
        );
    }

    var network = new vis.Network(
        document.getElementById("viewArea"),
        {
            nodes : new vis.DataSet(nodes),
            edges : new vis.DataSet(arcs)
        },
        {
            nodes: {borderWidth: 2},
            interaction: {hover: true}
        }
    );
}

function isArcInPath(arc, path) {
    if (arc == undefined || path == undefined) {
        return false;
    }

    for (var i = 0; i < path.length - 1; ++i) {
        if (path[i] == arc.a && path[i + 1] == arc.b ||
            path[i] == arc.b && path[i + 1] == arc.a)
        return true;
    }

    return false;
}

function onSaveGraphButtonClicked() {
    var graph = getGraphJSONFromInput();

    if (graph) {
        $.post(
            '/graph/',
            {graph: JSON.stringify(graph)},
            function(pk) {
                alert('Saved with pk = ' + pk);
            }//,
            //function(errorText) {
            //    alert("Can't save graph :( Error: " + errorText)
            //}
        );
    } else {
        alert('Bad graph input! Please, check it');
    }
}

function getGraphJSONFromInput() {
    var input = document.getElementById("graphInputArea").value;

    if (Constants.graphInputRegExp.test(input)) {
        input = input.split(';');
        var graph = {
            nodes: [],
            arcs: []
        };

        var nodes = input[0].replace(/\s*/, '').replace('nodes:', '').split(',');

        for (var i = 0; i < nodes.length; ++i) {
            var xy = nodes[i].replace(/[\d]+\[/, '').replace(']', '').split(':');
            graph.nodes.push({
                value: parseInt(nodes[i].replace(/\[.*]/, '')),
                x: parseInt(xy[0]),
                y: parseInt(xy[1])
            });
        }

        var arcs = input[1].replace(/\s*/, '').replace('arcs:', '').split(',');

        for (var j = 0; j < arcs.length; ++j) {
            var arcNodes = arcs[j].replace(/\[\d+]/, '').split('->');
            graph.arcs.push({
                a: parseInt(arcNodes[0]),
                b: parseInt(arcNodes[1]),
                w: parseInt(arcs[j].replace(/\d+->\d+\[/, '').replace(']', ''))
            });
        }

        return graph;
    }

    return undefined;
}
