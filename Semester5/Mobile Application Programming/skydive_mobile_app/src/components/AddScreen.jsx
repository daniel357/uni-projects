import React, {useState} from "react";
import {Alert, ScrollView} from "react-native";
import {Button, TextInput} from "react-native-paper";
import DateTimePicker from "@react-native-community/datetimepicker";
import {styles} from "./MainScreen";
import SkydiveJump from "../SkydivingJump";

// interface AddScreenProps {
//   navigation: any;
//   route: any;
// }

const AddScreen = (props) => {
    const [title, setTitle] = useState("");
    const [canopy, setCanopy] = useState("");
    const [plane, setPlane] = useState("");
    const [dropzone, setDropzone] = useState("");
    const [datetime, setDatetime] = useState(new Date());
    const [altitude, setAltitude] = useState("");
    const [description, setDescription] = useState("");

    const handleAdd = () => {
        if (!Number.isInteger(Number(altitude))) {
            Alert.alert("Invalid input", "Altitude should be a number!");
            return;
        }

        if (
            title === "" ||
            canopy === "" ||
            plane == "" ||
            dropzone == "" ||
            !datetime ||
            altitude == ""
        ) {
            Alert.alert("Invalid input", "Make sure all fields are filled in!");
            return;
        }

        const newJump = new SkydiveJump(
            0,
            title,
            canopy,
            plane,
            dropzone,
            datetime,
            parseFloat(altitude),
            description
        );
        props.navigation.navigate("Jump List", {newJumpRecord: newJump});
    };

    return (
        <ScrollView style={styles.container}>
            <TextInput
                label="Title"
                placeholder="Enter Jump Title"
                style={styles.textInput}
                underlineColor="transparent"
                onChangeText={(text) => setTitle(text)}
            />
            <TextInput
                label="Canopy"
                placeholder="Enter Canopy Type"
                style={styles.textInput}
                underlineColor="transparent"
                onChangeText={(text) => setCanopy(text)}
            />
            <TextInput
                label="Plane"
                placeholder="Enter Plane Type"
                style={styles.textInput}
                underlineColor="transparent"
                onChangeText={(text) => setPlane(text)}
            />
            <TextInput
                label="Dropzone"
                placeholder="Enter Dropzone Name"
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
                placeholder="Enter Altitude"
                style={styles.textInput}
                underlineColor="transparent"
                onChangeText={(text) => setAltitude(text)}
            />
            <TextInput
                label="Description"
                placeholder="Enter Description"
                style={styles.textInput}
                underlineColor="transparent"
                onChangeText={(text) => setDescription(text)}
            />
            <Button
                style={styles.button}
                labelStyle={{color: "white"}}
                onPress={handleAdd}
            >
                Add Jump Record
            </Button>
        </ScrollView>
    );
};

export default AddScreen;
