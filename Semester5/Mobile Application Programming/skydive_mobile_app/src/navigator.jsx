import React from "react";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { NavigationContainer } from "@react-navigation/native";
import MainScreen from "./components/MainScreen";
import AddScreen from "./components/AddScreen";
import DeleteScreen from "./components/DeleteScreen";
import EditScreen from "./components/EditScreen";

const { Navigator, Screen } = createNativeStackNavigator();

const AppNavigator = () => (
  <NavigationContainer>
    <Navigator initialRouteName="Jumps List">
      <Screen name="Jump List" component={MainScreen} />
      <Screen name="Add" component={AddScreen} />
      <Screen name="Delete" component={DeleteScreen} />
      <Screen name="Edit" component={EditScreen} />
    </Navigator>
  </NavigationContainer>
);

export default AppNavigator;
