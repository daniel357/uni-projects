import React, { useState } from "react";
import { Alert, ScrollView } from "react-native";
import { Button, TextInput } from "react-native-paper";
import DateTimePicker from "@react-native-community/datetimepicker";
import { styles } from "./MainScreen";

const EditScreen = (props) => {
  const selectedJump = props.route.params.jumpKey;

  const [title, setTitle] = useState(selectedJump.title);
  const [canopy, setCanopy] = useState(selectedJump.canopy);
  const [plane, setPlane] = useState(selectedJump.plane);
  const [dropzone, setDropzone] = useState(selectedJump.dropzone);
  const [datetime, setDatetime] = useState(new Date(selectedJump.datetime));
  const [altitude, setAltitude] = useState(selectedJump.altitude.toString());
  const [description, setDescription] = useState(selectedJump.description);

  const handleUpdate = () => {
    if (!Number.isInteger(Number(altitude))) {
      Alert.alert("Invalid input", "Altitude should be a number!");
      return;
    }

    if (
      title == "" ||
      canopy == "" ||
      plane == "" ||
      dropzone == "" ||
      !datetime ||
      altitude == ""
    ) {
      Alert.alert("Invalid input", "Make sure all fields are filled in!");
      return;
    }

    selectedJump.title = title;
    selectedJump.canopy = canopy;
    selectedJump.plane = plane;
    selectedJump.dropzone = dropzone;
    selectedJump.datetime = datetime;
    selectedJump.altitude = parseFloat(altitude);
    selectedJump.description = description;

    props.navigation.navigate("Jump List", { updatedJump: selectedJump });
  };

  return (
    <ScrollView style={styles.container}>
      <TextInput
        label="Title"
        value={title}
        style={styles.textInput}
        underlineColor="transparent"
        onChangeText={(text) => setTitle(text)}
      />
      <TextInput
        label="Canopy"
        value={canopy}
        style={styles.textInput}
        underlineColor="transparent"
        onChangeText={(text) => setCanopy(text)}
      />
      <TextInput
        label="Plane"
        value={plane}
        style={styles.textInput}
        underlineColor="transparent"
        onChangeText={(text) => setPlane(text)}
      />
      <TextInput
        label="Dropzone"
        value={dropzone}
        style={styles.textInput}
        underlineColor="transparent"
        onChangeText={(text) => setDropzone(text)}
      />
      <DateTimePicker
        testID="dateTimePicker"
        value={datetime}
        mode="datetime"
        is24Hour={true}
        display="default"
        onChange={(event, selectedDate) =>
          setDatetime(selectedDate || datetime)
        }
      />
      <TextInput
        label="Altitude"
        value={altitude}
        style={styles.textInput}
        underlineColor="transparent"
        onChangeText={(text) => setAltitude(text)}
      />
      <TextInput
        label="Description"
        value={description}
        style={styles.textInput}
        underlineColor="transparent"
        onChangeText={(text) => setDescription(text)}
      />
      <Button
        style={styles.button}
        labelStyle={{ color: "white" }}
        onPress={handleUpdate}
      >
        Update Jump Record
      </Button>
    </ScrollView>
  );
};

export default EditScreen;
