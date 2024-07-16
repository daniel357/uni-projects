import { View, Text } from "react-native";
import { Button } from "react-native-paper";
import { styles } from "./MainScreen";

// interface DeleteScreenProps {
//   navigation: any;
//   route: any;
// }

const DeleteJump = (props) => {
  // Assuming the selected jump is passed in the route params under the key 'jumpKey'
  const selectedJump = props.route.params.jumpKey;

  const handleCancel = () => {
    props.navigation.navigate("Jump List");
  };
  const handleDelete = () => {
    props.navigation.navigate("Jump List", { jumpIndex: selectedJump.id });
  };

  return (
    <View style={styles.container}>
      <Text>
        Are you sure you want to delete this jump record? This action will be
        permanent!
      </Text>
      <View style={{ flexDirection: "row", justifyContent: "space-between" }}>
        <Button
          onPress={handleCancel}
          labelStyle={{ color: "white" }}
          style={styles.button}
        >
          CANCEL
        </Button>
        <Button
          onPress={handleDelete}
          labelStyle={{ color: "white" }}
          style={styles.button}
        >
          DELETE
        </Button>
      </View>
    </View>
  );
};

export default DeleteJump;
