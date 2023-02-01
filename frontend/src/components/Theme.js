import { createTheme } from '@mui/material/styles';
import BebasNeueRegular from '../../static/fonts/BebasNeueRegular.ttf';

const font = {
  fontFamily: `'Bebas Neue', sans-serif`,
  src: `url(${BebasNeueRegular}) format('truetype')`,
};

const typography = {
  fontFamily: font.fontFamily,
  fontWeight: 'normal',
  h1: { fontFamily: font.fontFamily },
  h2: { fontFamily: font.fontFamily },
  h3: { fontFamily: font.fontFamily },
  h4: { fontFamily: font.fontFamily },
  h5: { fontFamily: font.fontFamily },
  h6: { fontFamily: font.fontFamily },
  body1: { fontFamily: font.fontFamily },
  body2: { fontFamily: font.fontFamily },
  subtitle1: { fontFamily: font.fontFamily },
  subtitle2: { fontFamily: font.fontFamily },
  overline: { fontFamily: font.fontFamily },
};

const theme = createTheme({
  palette: {
    primary: { main: '#076AE0' },
    secondary: { main: '#59bbff' },
    error: { main: '#ff0000' },
  },
  typography,
});

export default theme;
