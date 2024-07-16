import * as React from 'react';
import { Provider } from 'react-redux';
import Head from 'next/head';
import { AppProps } from 'next/app';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { CacheProvider, EmotionCache } from '@emotion/react';
import store from '@redux/store';
import { PersistGate } from 'redux-persist/integration/react';
import { SWRConfig } from 'swr';
import { persistStore } from 'redux-persist';

import theme from '../src/theme';
import createEmotionCache from '../src/createEmotionCache';
import '../styles/globals.css';
import LoadingSpinner from '../src/components/LoadingSpinner/LoadingSpinner';
import { config } from '@fortawesome/fontawesome-svg-core';
import '@fortawesome/fontawesome-svg-core/styles.css';
config.autoAddCss = false;
interface MyAppProps extends AppProps {
  emotionCache?: EmotionCache;
}

const clientSideEmotionCache = createEmotionCache();

const persistor = persistStore(store);

export default function MyApp(props: MyAppProps) {
  const { Component, emotionCache = clientSideEmotionCache, pageProps } = props;

  return (
    <CacheProvider value={emotionCache}>
      <Head>
        <title>Project Name</title>
        <meta name="viewport" content="initial-scale=1, width=device-width" />
      </Head>
      <ThemeProvider theme={theme}>
        <Provider store={store}>
          <PersistGate persistor={persistor}>
            <CssBaseline />
            <LoadingSpinner />
            <SWRConfig value={{ refreshInterval: 0, revalidateOnFocus: false }}>
              <Component {...pageProps} />
            </SWRConfig>
          </PersistGate>
        </Provider>
      </ThemeProvider>
    </CacheProvider>
  );
}
