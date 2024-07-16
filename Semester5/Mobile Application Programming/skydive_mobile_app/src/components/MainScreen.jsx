import React, {useEffect, useState} from "react";
import {Alert, ScrollView, StyleSheet, Text, View} from "react-native";
import {Card, IconButton, Title} from "react-native-paper";
import * as SQLite from "expo-sqlite";
import SkydiveJump from "../SkydivingJump";

// const ip = `192.168.100.54:8000`; // wifi from home
const ip = `172.30.111.242:8000` // mateinfo

const url = `http://${ip}`;

export const renderJumpCard = ({jump, props}) => {
    const handleOnEditButton = () => {
        props.navigation.navigate("Edit", {jumpKey: jump});
    };
    const handleOnDeleteButton = () => {
        props.navigation.navigate("Delete", {jumpKey: jump});
    };

    return (
        <>
            <Card key={jump.getId()} style={styles.card}>
                <Card.Content>
                    <Title>{jump.getTitle()}</Title>
                </Card.Content>
                <Card.Actions>
                    <IconButton
                        icon="pencil"
                        iconColor="white"
                        size={20}
                        onPress={handleOnEditButton}
                        style={styles.iconButton}
                    />
                    <IconButton
                        icon="delete"
                        iconColor="white"
                        size={20}
                        onPress={handleOnDeleteButton}
                        style={styles.iconButton}
                    />
                </Card.Actions>
            </Card>
        </>
    );
};

const MainScreen = (props) => {
    const updatedJump = props.route.params?.updatedJump;
    const jumpIndex = props.route.params?.jumpIndex;
    const newJump = props.route.params?.newJumpRecord;

    const [jumps, setJumps] = useState([]);

    const db = SQLite.openDatabase("jumps.db");
    // db.transaction(tx => {tx.executeSql('DELETE FROM jumps')});

    const [isLoading, setIsLoading] = useState(true);

    const addJump = (newJump) => {
        const requestBody = {
            title: newJump.getTitle(),
            canopy: newJump.getCanopy(),
            plane: newJump.getPlane(),
            dropzone: newJump.getDropzone(),
            datetime: newJump.getDateTime(),
            altitude: newJump.getAltitude(),
            description: newJump.getDescription(),
        };

        fetch(`${url}/jumps/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestBody),
        })
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                if (data.id) {
                    // Update the jump's ID with the one received from the server
                    newJump.resetId(data.id);
                    db.transaction((tx) => {
                        tx.executeSql(
                            "INSERT INTO jumps (id, title, canopy, plane, dropzone, datetime, altitude, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            [
                                newJump.getId(),
                                newJump.getTitle(),
                                newJump.getCanopy(),
                                newJump.getPlane(),
                                newJump.getDropzone(),
                                newJump.getDateTime().toISOString(),
                                newJump.getAltitude(),
                                newJump.getDescription(),
                            ],
                            (txObj, resultSet) => {
                                setJumps((currentJumps) => [...currentJumps, newJump]);
                            },
                            (txObj, error) => {
                                console.log("Error inserting jump record: ", error);
                                Alert.alert("Data Persistence Error", "Insert Object error!");
                                return false;
                            }
                        );
                    });
                } else {
                    console.error("Failed to add jump on the server");
                    Alert.alert("Server Error", "Failed to add jump on the server");
                }
            })
            .catch((error) => {
                if (
                    error.toString().includes("TypeError: Network request failed") ||
                    error.toString().includes("WebSocket connection closed ")
                ) {
                    console.log("Inserting from server failed, doing from local DB");

                    db.transaction((tx) => {
                        tx.executeSql(
                            "SELECT MIN(id) AS minId FROM jumps",
                            [],
                            (txObj, resultSet) => {
                                const minId = resultSet.rows.item(0).minId;
                                console.log("Minimum ID:", minId);

                                const minimumId = Math.min(minId, 0);
                                console.log("Minimum ID (adjusted):", minimumId);

                                const currentId = minimumId - 1;
                                console.log("Current ID:", currentId);

                                newJump.resetId(currentId);

                                db.transaction((tx) => {
                                    tx.executeSql(
                                        "INSERT INTO jumps (id, title, canopy, plane, dropzone, datetime, altitude, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                        [
                                            currentId,
                                            newJump.getTitle(),
                                            newJump.getCanopy(),
                                            newJump.getPlane(),
                                            newJump.getDropzone(),
                                            newJump.getDateTime().toISOString(),
                                            newJump.getAltitude(),
                                            newJump.getDescription(),
                                        ],
                                        (txObj, resultSet) => {
                                            setJumps((currentJumps) => [...currentJumps, newJump]);
                                        },
                                        (txObj, error) => {
                                            console.log("Error inserting jump record: ", error);
                                            Alert.alert(
                                                "Data Persistence Error",
                                                "Insert Object error!"
                                            );
                                            return false;
                                        }
                                    );
                                });
                            },
                            (txObj, error) => {
                                console.log("Error selecting minimum ID:", error);
                                return false;
                            }
                        );
                    });
                }
            });
    };

    const updateJump = (updatedJump) => {
        const requestBody = {
            id: updatedJump.getId(),
            title: updatedJump.getTitle(),
            canopy: updatedJump.getCanopy(),
            plane: updatedJump.getPlane(),
            dropzone: updatedJump.getDropzone(),
            datetime: updatedJump.getDateTime(),
            altitude: updatedJump.getAltitude(),
            description: updatedJump.getDescription(),
        };

        fetch(`${url}/jumps/${updatedJump.getId()}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestBody),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.id) {
                    db.transaction((tx) => {
                        tx.executeSql(
                            "UPDATE jumps SET title=?, canopy=?, plane=?, dropzone=?, datetime=?, altitude=?, description=? WHERE id=?",
                            [
                                updatedJump.getTitle(),
                                updatedJump.getCanopy(),
                                updatedJump.getPlane(),
                                updatedJump.getDropzone(),
                                updatedJump.getDateTime().toISOString(),
                                updatedJump.getAltitude(),
                                updatedJump.getDescription(),
                                updatedJump.getId(),
                            ],
                            (txObj, resultSet) => {
                                if (resultSet.rowsAffected > 0) {
                                    setJumps((currentJumps) => {
                                        const objIndex = currentJumps.findIndex(
                                            (obj) => obj.getId() === updatedJump.getId()
                                        );
                                        if (objIndex !== -1) {
                                            currentJumps[objIndex] = updatedJump;
                                        }
                                        return [...currentJumps];
                                    });
                                }
                            },
                            (txObj, error) => {
                                console.log("Error updating jump record: ", error);
                                Alert.alert("Data Persistence Error", "Update Object error!");
                                return false;
                            }
                        );
                    });
                } else {
                    console.error("Failed to update jump on the server");
                    Alert.alert("Server Error", "Failed to update jump on the server");
                }
            })
            .catch((error) => {
                if (
                    error.toString().includes("TypeError: Network request failed") ||
                    error.toString().includes("WebSocket connection closed ")
                ) {
                    console.log("Updating from server failed, updating in local DB");
                    db.transaction((tx) => {
                        tx.executeSql(
                            "UPDATE jumps SET title=?, canopy=?, plane=?, dropzone=?, datetime=?, altitude=?, description=?, flag=? WHERE id=?",
                            [
                                updatedJump.getTitle(),
                                updatedJump.getCanopy(),
                                updatedJump.getPlane(),
                                updatedJump.getDropzone(),
                                updatedJump.getDateTime().toISOString(),
                                updatedJump.getAltitude(),
                                updatedJump.getDescription(),
                                whatFlag,
                                updatedJump.getId(),
                            ],
                            (txObj, resultSet) => {
                                if (resultSet.rowsAffected > 0) {
                                    setJumps((currentJumps) => {
                                        const objIndex = currentJumps.findIndex(
                                            (obj) => obj.getId() === updatedJump.getId()
                                        );
                                        if (objIndex !== -1) {
                                            currentJumps[objIndex] = updatedJump;
                                        }
                                        return [...currentJumps];
                                    });
                                }
                            },
                            (txObj, error) => {
                                console.log("Error updating jump record: ", error);
                                Alert.alert("Data Persistence Error", "Update Object error!");
                                return false;
                            }
                        );
                    });
                }
            });
    };

    const deleteJump = (jumpId) => {
        fetch(`${url}/jumps/${jumpId}/`, {
            method: "DELETE",
        })
            .then((response) => {
                if (response.status === 204) {
                    db.transaction((tx) => {
                        tx.executeSql(
                            "DELETE FROM jumps WHERE id=?",
                            [jumpId],
                            (txObject, resultSet) => {
                                if (resultSet.rowsAffected > 0) {
                                    setJumps((currentJumps) => {
                                        const objIndex = currentJumps.findIndex(
                                            (obj) => obj.getId() === jumpId
                                        );
                                        currentJumps.splice(objIndex, 1);
                                        return [...currentJumps];
                                    });
                                }
                            },
                            (txObj, error) => {
                                console.log("Error deleting jump record: ", error);
                                Alert.alert("Data Persistence Error", "Delete Object error!");
                                return false;
                            }
                        );
                    });
                } else {
                    console.error("Failed to delete jump on the server");
                    Alert.alert("Server Error", "Failed to delete jump on the server");
                }
            })
            .catch((error) => {
                if (
                    error.toString().includes("TypeError: Network request failed") ||
                    error.toString().includes("WebSocket connection closed ")
                ) {
                    console.log("Deleting from server failed, doing from local DB");
                    console.log("DELETE JUMP ID: ", jumpId);

                    if (jumpId < 0) {
                        db.transaction((tx) => {
                            tx.executeSql(
                                "DELETE FROM jumps WHERE id=?",
                                [jumpId],
                                (txObj, resultSet) => {
                                    if (resultSet.rowsAffected > 0) {
                                        setJumps((currentJumps) => {
                                            const objIndex = currentJumps.findIndex(
                                                (obj) => obj.getId() === jumpId
                                            );
                                            currentJumps.splice(objIndex, 1);
                                            return [...currentJumps];
                                        });
                                    }
                                }
                            );
                        });
                    } else {
                        db.transaction((tx) => {
                            tx.executeSql(
                                "UPDATE jumps SET flag = 3 WHERE id=?",
                                [jumpId],
                                (txObj, resultSet) => {
                                    if (resultSet.rowsAffected > 0) {
                                        setJumps((currentJumps) => {
                                            const objIndex = currentJumps.findIndex(
                                                (obj) => obj.getId() === jumpId
                                            );
                                            currentJumps.splice(objIndex, 1);
                                            return [...currentJumps];
                                        });
                                    }
                                }
                            );
                        });
                    }
                }
            });
    };

    ///WS

    const addJumpWS = (newJump) => {
        db.transaction((tx) => {
            tx.executeSql(
                "INSERT INTO jumps (id, title, canopy, plane, dropzone, datetime, altitude, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                [
                    newJump.getId(),
                    newJump.getTitle(),
                    newJump.getCanopy(),
                    newJump.getPlane(),
                    newJump.getDropzone(),
                    newJump.getDateTime().toISOString(),
                    newJump.getAltitude(),
                    newJump.getDescription(),
                ],
                (txObj, resultSet) => {
                    setJumps((currentJumps) => [...currentJumps, newJump]);
                },
                (txObj, error) => {
                    console.log("Error inserting jump record: ", error);
                    Alert.alert("Data Persistence Error", "Insert Object error!");
                    return false;
                }
            );
        });
    };

    const updateJumpWS = (updatedJump) => {
        db.transaction((tx) => {
            tx.executeSql(
                "UPDATE jumps SET title=?, canopy=?, plane=?, dropzone=?, datetime=?, altitude=?, description=? WHERE id=?",
                [
                    updatedJump.getTitle(),
                    updatedJump.getCanopy(),
                    updatedJump.getPlane(),
                    updatedJump.getDropzone(),
                    updatedJump.getDateTime().toISOString(),
                    updatedJump.getAltitude(),
                    updatedJump.getDescription(),
                    updatedJump.getId(),
                ],
                (txObj, resultSet) => {
                    if (resultSet.rowsAffected > 0) {
                        setJumps((currentJumps) => {
                            const objIndex = currentJumps.findIndex(
                                (obj) => obj.getId() === updatedJump.getId()
                            );
                            if (objIndex !== -1) {
                                currentJumps[objIndex] = updatedJump;
                            }
                            return [...currentJumps];
                        });
                    }
                },
                (txObj, error) => {
                    console.log("Error updating jump record: ", error);
                    Alert.alert("Data Persistence Error", "Update Object error!");
                    return false;
                }
            );
        });
    };

    const deleteJumpWS = (deletedJumpId) => {
        db.transaction((tx) => {
            tx.executeSql(
                "DELETE FROM jumps WHERE id=?",
                [deletedJumpId],
                (txObject, resultSet) => {
                    if (resultSet.rowsAffected > 0) {
                        setJumps((currentJumps) => {
                            const objIndex = currentJumps.findIndex(
                                (obj) => obj.getId() === deletedJumpId
                            );
                            if (objIndex !== -1) {
                                currentJumps.splice(objIndex, 1);
                            }
                            return [...currentJumps];
                        });
                    }
                },
                (txObj, error) => {
                    console.log("Error deleting jump record: ", error);
                    Alert.alert("Data Persistence Error", "Delete Object error!");
                    return false;
                }
            );
        });
    };

    const handleWebSocketMessage = (message) => {
        switch (message.action) {
            case "create":
                const newJump = new SkydiveJump(
                    message.jump.id,
                    message.jump.title,
                    message.jump.canopy,
                    message.jump.plane,
                    message.jump.dropzone,
                    new Date(message.jump.datetime), // datetime is sent as a string
                    message.jump.altitude,
                    message.jump.description
                );
                addJumpWS(newJump);
                break;
            case "update":
                const updatedJump = new SkydiveJump(
                    message.jump.id,
                    message.jump.title,
                    message.jump.canopy,
                    message.jump.plane,
                    message.jump.dropzone,
                    new Date(message.jump.datetime), //datetime is sent as a string
                    message.jump.altitude,
                    message.jump.description
                );
                updateJumpWS(updatedJump);
                break;
            case "delete":
                deleteJumpWS(message.jump.id);
                break;
            default:
                console.log("Received unknown message type", message.type);
        }
    };

    const fetchJumpsFromDB = () => {
        db.transaction((tx) => {
            tx.executeSql(
                "SELECT * FROM jumps WHERE flag != 3", // flag 3 = marked for deletion
                [],
                (_, {rows}) => {
                    const tempJumps = [];
                    for (let i = 0; i < rows.length; i++) {
                        tempJumps.push(
                            new SkydiveJump(
                                rows.item(i).id,
                                rows.item(i).title,
                                rows.item(i).canopy,
                                rows.item(i).plane,
                                rows.item(i).dropzone,
                                new Date(rows.item(i).datetime),
                                rows.item(i).altitude,
                                rows.item(i).description
                            )
                        );
                    }
                    setJumps([...tempJumps]); // Directly set the jumps from DB
                    setIsLoading(false);
                },
                (txObj, error) => {
                    console.log("Error fetching jumps from DB: ", error);
                    Alert.alert("Data Persistence Error", "Fetching data error!");
                    return false;
                }
            );
        });
    };

    const syncJumpsWithServer = () => {
        db.transaction((tx) => {
            tx.executeSql(
                "SELECT * FROM jumps WHERE flag = 1 OR flag = 2 OR flag = 3",
                [],
                (_, {rows}) => {
                    const jumpsForServer = [];
                    for (let i = 0; i < rows.length; i++) {
                        jumpsForServer.push({
                            jump: new SkydiveJump(
                                rows.item(i).id,
                                rows.item(i).title,
                                rows.item(i).canopy,
                                rows.item(i).plane,
                                rows.item(i).dropzone,
                                new Date(rows.item(i).datetime), // Assuming datetime is stored as a string
                                rows.item(i).altitude,
                                rows.item(i).description
                            ),
                            flag: rows.item(i).flag,
                        });
                    }

                    jumpsForServer.forEach((jumpWithFlag) => {
                        const jump = jumpWithFlag.jump;
                        const flag = jumpWithFlag.flag;

                        switch (flag) {
                            case 1: // POST
                                const requestBodyPost = {
                                    title: jump.getTitle(),
                                    canopy: jump.getCanopy(),
                                    plane: jump.getPlane(),
                                    dropzone: jump.getDropzone(),
                                    datetime: jump.getDateTime().toISOString(),
                                    altitude: jump.getAltitude(),
                                    description: jump.getDescription(),
                                };

                                fetch(`${url}/jumps/`, {
                                    // Update the endpoint to match your API
                                    method: "POST",
                                    headers: {
                                        "Content-Type": "application/json",
                                    },
                                    body: JSON.stringify(requestBodyPost),
                                })
                                    .then((response) => response.json())
                                    .then((data) => {
                                        const addedJump = jumpWithFlag.jump;
                                        if (data.id) {
                                            const newServerId = data.id;
                                            const oldLocalId = addedJump.getId();

                                            // Update local DB
                                            db.transaction((tx) => {
                                                tx.executeSql(
                                                    "UPDATE jumps SET id = ?, flag = 0 WHERE id = ?", // Update the table and field names
                                                    [newServerId, oldLocalId],
                                                    (_, resultSet) => {
                                                        if (resultSet.rowsAffected > 0) {
                                                            console.log(
                                                                `Jump ID updated from ${oldLocalId} to ${newServerId}`
                                                            );
                                                            setJumps((currentJumps) => {
                                                                const objIndex = currentJumps.findIndex(
                                                                    (obj) => obj.getId() === oldLocalId
                                                                );
                                                                if (objIndex != -1) {
                                                                    currentJumps[objIndex].resetId(newServerId);
                                                                }
                                                                return [...currentJumps];
                                                            });
                                                        } else {
                                                            console.log(
                                                                `Failed to update jump ID in local DB`
                                                            );
                                                        }
                                                    },
                                                    (_, error) => {
                                                        console.log("Error updating jump ID:", error);
                                                        return false;
                                                    }
                                                );
                                            });
                                        } else {
                                            console.log("Failed to add jump on the server");
                                        }
                                    })
                                    .catch((error) => {
                                        console.log("Error making POST request:", error);
                                    });
                                break;

                            case 2: // PUT
                                const requestBodyPut = {
                                    id: jump.getId(),
                                    title: jump.getTitle(),
                                    canopy: jump.getCanopy(),
                                    plane: jump.getPlane(),
                                    dropzone: jump.getDropzone(),
                                    datetime: jump.getDateTime().toISOString(),
                                    altitude: jump.getAltitude(),
                                    description: jump.getDescription(),
                                };

                                fetch(`${url}/jumps/${jump.getId()}/`, {
                                    method: "PUT",
                                    headers: {
                                        "Content-Type": "application/json",
                                    },
                                    body: JSON.stringify(requestBodyPut),
                                })
                                    .then((response) => response.json())
                                    .then((data) => {
                                        const updatedJump = jumpWithFlag.jump;
                                        db.transaction((tx) => {
                                            tx.executeSql(
                                                "UPDATE jumps SET flag = 0 WHERE id = ?", // Update the table and field names
                                                [updatedJump.getId()],
                                                (_, {rowsAffected}) => {
                                                    if (rowsAffected > 0) {
                                                        console.log(
                                                            "Flag updated successfully for jump ID:",
                                                            updatedJump.getId()
                                                        );
                                                    } else {
                                                        console.log(
                                                            "Failed to update flag for jump ID:",
                                                            updatedJump.getId()
                                                        );
                                                    }
                                                },
                                                (_, error) => {
                                                    console.log(
                                                        "Error updating flag for jump ID:",
                                                        updatedJump.getId(),
                                                        error
                                                    );
                                                    return false;
                                                }
                                            );
                                        });
                                    })
                                    .catch((error) => {
                                        console.log("Error making PUT request:", error);
                                    });
                                break;

                            case 3: // DELETE
                                fetch(`${url}/jumps/${jump.getId()}/`, {
                                    // Update the endpoint to match your API
                                    method: "DELETE",
                                })
                                    .then((response) => {
                                        if (response.status === 204) {
                                            const deletedJump = jumpWithFlag.jump;
                                            console.log(deletedJump.getId());
                                            db.transaction((tx) => {
                                                tx.executeSql(
                                                    "DELETE FROM jumps WHERE id = ?", // Update the table name
                                                    [deletedJump.getId()],
                                                    (_, resultSet) => {
                                                        if (resultSet.rowsAffected > 0) {
                                                            console.log(
                                                                `Jump with ID ${deletedJump.getId()} deleted from local DB`
                                                            );
                                                        } else {
                                                            console.log(
                                                                `No jump found with ID ${deletedJump.getId()} in local DB`
                                                            );
                                                        }
                                                    },
                                                    (txObj, error) => {
                                                        console.log(
                                                            "Error deleting jump from local DB:",
                                                            error
                                                        );
                                                        return false;
                                                    }
                                                );
                                            });
                                        } else {
                                            throw new Error("Server responded with an error!");
                                        }
                                    })
                                    .catch((error) => {
                                        console.log(
                                            "Error making DELETE request or deleting from local DB:",
                                            error
                                        );
                                    });
                                break;
                            default:
                                break;
                        }
                    });
                },
                (txObj, error) => {
                    console.log("Error fetching jumps for sync:", error);
                    return false;
                }
            );
        });
    };

    useEffect(() => {
        db.transaction((tx) => {
            tx.executeSql(
                "CREATE TABLE IF NOT EXISTS jumps (id INTEGER PRIMARY KEY, title TEXT, canopy TEXT, plane TEXT, dropzone TEXT, datetime TEXT, altitude INTEGER, description TEXT, flag INTEGER DEFAULT 0)",
                [],
                () => {
                    fetch(`${url}/jumps/`, {method: "GET"})
                        .then((response) => response.json())
                        .then((data) => {
                            if (data.length === 0) {
                                console.log('no data')
                                setIsLoading(false);
                            }
                            if (data) {
                                data.forEach((jump) => {
                                    // update the in-memory list with data from server
                                    const updatedJump = new SkydiveJump(
                                        jump.id,
                                        jump.title,
                                        jump.canopy,
                                        jump.plane,
                                        jump.dropzone,
                                        new Date(jump.datetime),
                                        jump.altitude,
                                        jump.description
                                    );
                                    setJumps((prevJumps) => [...prevJumps, updatedJump]);
                                    setIsLoading(false);
                                });
                            }
                        })
                        .catch((error) => {
                            console.log(error)
                            if (
                                error.toString().includes("TypeError: Network request failed")
                            ) {
                                console.log(
                                    "Fetching from server failed, fetching from local DB"
                                );
                                fetchJumpsFromDB();
                            }
                        });
                },
                (txObj, error) => {
                    console.log("Error setting up jumps table: ", error);
                    Alert.alert("Data Persistence Error", "Creating table error!");
                    return false;
                }
            );
        });
    }, []);

    useEffect(() => {
        let ws;

        const connectWebSocket = () => {
            ws = new WebSocket(`ws://${ip}/ws/jumps/`);

            ws.onopen = () => {
                console.log("WebSocket connection opened");
                syncJumpsWithServer(); // This function should handle syncing jumps with the server
            };

            ws.onmessage = (e) => {
                const message = JSON.parse(e.data);
                handleWebSocketMessage(message); // Ensure this function handles jump-related messages
            };

            ws.onerror = (e) => {
                console.error("WebSocket encountered an error", e.message);
            };

            ws.onclose = (e) => {
                console.log("WebSocket connection closed", e.code, e.reason);
                // Try to reconnect after a short delay
                setTimeout(() => connectWebSocket(), 3000);
            };
        };

        connectWebSocket();

        return () => {
            if (ws) {
                ws.close();
            }
        };
    }, []);

    useEffect(() => {
        if (updatedJump !== undefined) {
            updateJump(updatedJump);
        }

        if (jumpIndex !== undefined) {
            deleteJump(jumpIndex);
        }

        if (newJump !== undefined) {
            addJump(newJump);
        }
    }, [updatedJump, jumpIndex, newJump]);

    const handleOnAddJumpButton = () => {
        props.navigation.navigate("Add");
    };

    if (isLoading) {
        return (
            <View style={styles.container}>
                <Text>Loading info...</Text>
            </View>
        );
    }

    return (
        <ScrollView style={styles.container}>
            {jumps.map((jump) => renderJumpCard({jump, props}))}
            <IconButton
                icon="plus-circle"
                iconColor="grey"
                size={50}
                onPress={handleOnAddJumpButton}
                style={styles.centreIcon}
            />
        </ScrollView>
    );
};

export const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16,
    },
    card: {
        marginBottom: 30,
        backgroundColor: "#8BC6FC",
        fontSize: 20,
    },
    image: {
        flex: 1,
        justifyContent: "center",
    },
    iconButton: {
        backgroundColor: "grey",
    },
    centreIcon: {
        alignSelf: "center",
        marginBottom: 50,
    },
    button: {
        backgroundColor: "grey",
        alignSelf: "center",
        marginBottom: 50,
        color: "white",
        marginStart: 50,
        marginEnd: 50,
        marginTop: 50,
    },
    textInput: {
        backgroundColor: "#8BC6FC",
        marginBottom: 30,
        height: 80,
        fontSize: 20,
        borderRadius: 8,
    },
});

export default MainScreen;
