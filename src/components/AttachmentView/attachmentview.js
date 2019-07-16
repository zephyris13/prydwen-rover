import Paper from "@material-ui/core/Paper";
import React, { Component } from "react";
import Config from "../../config.json";
import "../../App.css";

class AttachmentView extends Component {
  constructor(props) {
    super(props);
    this.state = {cameraUrl: "http://" + Config["camera_host"] + ":" + Config["camera_port"] + "/?action=stream"};
  }

  render() {
    return (
      <Paper className="Video">
        <p>Attachment View</p>
        <img style={{ paddingBottom: "20px" }} src={this.state.cameraUrl} alt={this.state.cameraUrl} />
      </Paper>
    );
  }
}

export default AttachmentView;