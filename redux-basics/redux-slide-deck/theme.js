import { yellow } from 'mdx-deck/themes'
import okaidia from 'react-syntax-highlighter/styles/prism/okaidia'

export default {
  ...yellow,
  prism: {
    style: okaidia
  },
  color: {
      ...yellow.colors,
      text: 'red',

  }
}