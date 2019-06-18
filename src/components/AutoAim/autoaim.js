import Paper from "@material-ui/core/Paper";
import Switch from "@material-ui/core/Switch";
import React, { Component } from "react";
import "../../App.css";

class AutoAim extends Component {
  constructor(props) {
    super(props);
    this.state = {
      autoaimChecked: false,
    };
  }

  handleChange = name => event => {
    this.setState({ [name]: event.target.checked });
  };

  render() {
    return (
        <Paper className="AutoAim">
          <p>Auto Aim</p>
          <Switch
            color="secondary"
            checked={this.state.autoaimChecked}
            onChange={this.handleChange("autoaimChecked")}
            value=""
          />
        </Paper>
      );
    }
  }
  
  export default AutoAim;