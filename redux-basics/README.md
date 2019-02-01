# Redux Basics

## Deck

h4i-redux.now.sh

## Explanations


Let's say you have an peach. You initial state of the peach is
```javascript
const initialPeach = {
  dirty: true, 
  remainingBites: 5, 
  color: 'orange',
};
```

You can do things to the peach with actions, so we want to define the actions. 

```javascript
const WASH = {type: 'WASH'};
const EAT = {type: 'EAT', bites: 2};
const ROT = {type: 'ROT'};
```

We want to define a reduce to tell redux how to handle these actions

```javascript 
function peachReducer(state = initialPeach, action) {
  switch(action.type) {
    case 'WASH':
      return {...state, dirty: false};
    case 'EAT':
      return {
        ...state,
        remainingBites: Math.max(0, state.remainingBites - action.bites)
      };
    case 'ROT':
      return {...state, color: 'brown'};
    default:
      return state;
  }
}

```



Every time we want to change the state of the peach, we dispatch an action. This calls the corresponding reducer which handles changing the state. 

Redux isolates all state changes in the reducers, which makes it easier to manage as the app scales. 

We also want to put this into a universal store. 
```javascript 

const store = Redux.createStore(peachReducer, initialPeach);
```

And we can use ```store.getState()```  to get a json object with the stat eof the current object. 

You can also subscribe to any changes of the peach.

```javascript
function handleChange() {
  const currentPeachState = store.getState();
  if (currentPeachState.color === 'orange') {
    console.log("Let's eat it");
  } else {
    console.log("Let's throw it out");
  }
}
store.subscribe(handleChange);
```
