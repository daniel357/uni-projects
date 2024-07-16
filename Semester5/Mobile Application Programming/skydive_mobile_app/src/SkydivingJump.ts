export default class SkydiveJump {
  private id: number;
  private title: string;
  private canopy: string;
  private plane: string;
  private dropzone: string;
  private datetime: Date;
  private altitude: number;
  private description: string;

  constructor(
    id: number,
    title: string,
    canopy: string,
    plane: string,
    dropzone: string,
    datetime: Date,
    altitude: number,
    description: string
  ) {
    this.id = id;
    this.title = title;
    this.canopy = canopy;
    this.plane = plane;
    this.dropzone = dropzone;
    this.datetime = datetime;
    this.altitude = altitude;
    this.description = description;
  }

  getId(): number {
    return this.id;
  }

  getTitle(): string {
    return this.title;
  }

  getCanopy(): string {
    return this.canopy;
  }

  getPlane(): string {
    return this.plane;
  }

  getDropzone(): string {
    return this.dropzone;
  }

  getDateTime(): Date {
    return this.datetime;
  }

  getAltitude(): number {
    return this.altitude;
  }

  getDescription(): string {
    return this.description;
  }

  resetId(newId: number) {
    this.id = newId;
  }

  // Additional method to update the jump details
  updateJump(
    title: string,
    canopy: string,
    plane: string,
    dropzone: string,
    datetime: Date,
    altitude: number,
    description: string
  ) {
    this.title = title;
    this.canopy = canopy;
    this.plane = plane;
    this.dropzone = dropzone;
    this.datetime = datetime;
    this.altitude = altitude;
    this.description = description;
  }
}
