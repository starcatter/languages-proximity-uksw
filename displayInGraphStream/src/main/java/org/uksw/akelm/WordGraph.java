package org.uksw.akelm;

import org.graphstream.graph.Edge;
import org.graphstream.graph.Node;
import org.graphstream.graph.implementations.SingleGraph;
import org.graphstream.stream.file.FileSinkImages;

import java.io.IOException;
import java.util.Arrays;
import java.util.DoubleSummaryStatistics;
import java.util.stream.Collectors;

public class WordGraph {
    private final boolean screenShot;
    String edgeStyle = "fill-color: rgba(%d, %d, %d, %d) ;" + "size:3px;" + "text-alignment: under; " + "text-color: white; " + "text-style: bold; " + "text-background-mode: rounded-box; " + "text-background-color: rgba(%d, %d, %d, %d); " + "text-padding: 1px; text-offset: 0px, 2px;";
    String nodeStyle = "fill-color: rgba(%d, %d, %d, %d) ;" + "size:15px;" + " text-alignment: under; " + "text-color: white; " + "text-style: bold; " + "text-background-mode: rounded-box; " + "text-background-color: rgba(%d, %d, %d, %d); " + "text-padding: 1px; text-offset: 0px, 2px;";
    boolean display;
    private SingleGraph wordGraph;

    public WordGraph(boolean display, boolean screenShot) {
        this.display = display;
        this.screenShot = screenShot;
        System.setProperty("org.graphstream.ui.renderer", "org.graphstream.ui.j2dviewer.J2DGraphRenderer");
    }

    public static void screenshot(SingleGraph myGraph, String filename) {
        if (myGraph != null) if (myGraph.getNodeCount() > 0) {
            FileSinkImages fsi = new FileSinkImages(FileSinkImages.OutputType.PNG, FileSinkImages.Resolutions.SVGA);
            fsi.setLayoutPolicy(FileSinkImages.LayoutPolicy.COMPUTED_FULLY_AT_NEW_IMAGE);
            fsi.setRenderer(FileSinkImages.RendererType.SCALA);
            try {
                fsi.writeAll(myGraph, filename);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    protected void createNode(String label, Double closeness, Double color) {
        Node node = wordGraph.addNode(label);
        String labelWithClosness = String.format("%s %.2g", label, closeness);
        node.setAttribute("ui.label", labelWithClosness);
        int blue = (int) (255 * (1 - color));
        int red = (int) (255 * color);
        String style = String.format(nodeStyle, red, 0, blue, 255, red, 0, blue, 255);
        node.setAttribute("ui.style", style);
    }

    protected void createEdge(String label0, String label1, Double weight, Double color) {
        Edge edge = wordGraph.addEdge(label0 + "--" + label1, label0, label1);
        edge.addAttribute("layout.weight", weight);
        edge.setAttribute("ui.label", String.format("%.3g", weight));
        int red = (int) (255 * (1 - color));
        int blue = (int) (255 * color);
        String style = String.format(edgeStyle, red, 0, blue, 128, red, 0, blue, 255);
        edge.setAttribute("ui.style", style);

    }

    public void showGraph(String[] label0List, String[] label1List, Double[] distArray, String[] nodesArray, Double[] closenessArray, String[] aggLabels) {
        wordGraph = new SingleGraph("graph");
        DoubleSummaryStatistics statisticsCloseness = Arrays.stream(closenessArray).collect(Collectors.summarizingDouble(e -> e));
        Double closenessMinVal = statisticsCloseness.getMin();
        Double closenessMaxVal = statisticsCloseness.getMax();
        for (int i = 0; i < nodesArray.length; i++) {
            String label = nodesArray[i];
            Double closeness = closenessArray[i];
            Double sclaed = (closeness - closenessMinVal) / (closenessMaxVal - closenessMinVal);
            createNode(label, closeness, sclaed);
        }
        DoubleSummaryStatistics statistics = Arrays.stream(distArray).collect(Collectors.summarizingDouble(e -> e));
        Double minVal = statistics.getMin();
        Double maxVal = statistics.getMax();

        for (int i = 0; i < distArray.length; i++) {
            Double dist = distArray[i];
            String label0 = label0List[i];
            String label1 = label1List[i];
            Double scaled = (dist - minVal) / (maxVal - minVal);
            createEdge(label0, label1, dist, scaled);
        }
        wordGraph.addAttribute("ui.antialias");
        if (this.display) {
            wordGraph.display(true);
        }
        if (this.screenShot) {
            String label_name = String.join("_", aggLabels);
            int max_len = 100;
            if (label_name.length() > max_len) {
                label_name = label_name.substring(0, max_len) + "_etc";
            }
            String node_name =  String.join("_", nodesArray);
            if (node_name.length() > max_len) {
                node_name = node_name.substring(0, max_len) + "_etc";
            }
            String filename = label_name + "_" + node_name + ".png";
            screenshot(wordGraph, filename);
        }


    }


}
