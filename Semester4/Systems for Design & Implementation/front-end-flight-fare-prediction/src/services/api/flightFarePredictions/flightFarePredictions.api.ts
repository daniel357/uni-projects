import { request } from '../api.helpers';
import { HttpResponse } from '../api.types';
import { EmailDto, FlightDto, PredictionResponseDto, StatisticsDto } from '../../../types/flight.types';

class FlightFarePredictionsApi {
  private static instance: FlightFarePredictionsApi | null = null;

  private constructor() {
  }

  static getInstance(): FlightFarePredictionsApi {
    if (!FlightFarePredictionsApi.instance) {
      FlightFarePredictionsApi.instance = new FlightFarePredictionsApi();
    }
    return FlightFarePredictionsApi.instance;
  }

  submitFlightDataForPrediction(data: FlightDto): Promise<HttpResponse<PredictionResponseDto>> {
    return request('/predict', 'post', data);
  }

  sendMailToUser(data: EmailDto): Promise<HttpResponse<void>> {
    return request('/mail', 'post', data);
  }

  getStatisticalDataAboutFlightPrices(): Promise<HttpResponse<StatisticsDto[]>> {
    return request('/statistics', 'get');
  }
}

export default FlightFarePredictionsApi.getInstance();
