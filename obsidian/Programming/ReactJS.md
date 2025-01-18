## How to think when using React
### 1. Start with a mock up
- Have a mockup of the UI that you will be building
[  

{ category: "Fruits", price: "$1", stocked: true, name: "Apple" },  

{ category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit" },  

{ category: "Fruits", price: "$2", stocked: false, name: "Passionfruit" },  

{ category: "Vegetables", price: "$2", stocked: true, name: "Spinach" },  

{ category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin" },  

{ category: "Vegetables", price: "$1", stocked: true, name: "Peas" }  

]
- Have some mockup data that you can put into the mockup UI
![[Pasted image 20250116105804.png]]
### 2. Break the UI into a component hierarchy
- Start by drawing boxes around every component and subcomponent in the mockup and start naming them. You can ask the designer if they have named the components in their design tool. 
- You can break them up based on 
	- design (like in a design tool)
	- programming (the number of functions or objects you need to build)
	- The type of data that you will receive can also give you an idea of the component structure of your UI
![[Pasted image 20250116110153.png]]

### 3. Build a static version in React
- Build the UI based on the component structure that you have outlined.
- Do not add any interactivity yet. e.g. states
- You can build it with a "top down" approach, starting from building the components higher up in the hierarchy or "bottom up" approach by building the smaller ones first and then going up from there.

### 4. Find the minimal but complete representation of UI state
- Figure out the absolute minimal representation of the state of your application needs and compute everything else on-demand. i.e. do not have too many states
- Questions to ask yourself:
	- Does it remain unchanged over time? If so, it isn't state
	- Is it passed in from a parent via props? If so, it isn't state
	- Can you compute it based on existing state or props in your component? If so, it definitely isn't state
Looking at the example:
1. The original list of products is **passed in as props, so it’s not state.**
2. The search text seems to be state since it changes over time and can’t be computed from anything.
3. The value of the checkbox seems to be state since it changes over time and can’t be computed from anything.
4. The filtered list of products **isn’t state because it can be computed** by taking the original list of products and filtering it according to the search text and value of the checkbox.

This means only the search text and the value of the checkbox are state! Nicely done!

### 5. Identify where your state should live
- Identify which component is responsible for changing this state, or owns this state (Where you declare it)
- . Often, you can put the state directly into their common parent.
- You can also put the state into some component above their common parent.
- If you can’t find a component where it makes sense to own the state, create a new component solely for holding the state and add it somewhere in the hierarchy above the common parent component.
- Now let’s run through our strategy for them:

1. **Identify components that use state:**
    - `ProductTable` needs to filter the product list based on that state (search text and checkbox value).
    - `SearchBar` needs to display that state (search text and checkbox value).
2. **Find their common parent:** The first parent component both components share is `FilterableProductTable`.
3. **Decide where the state lives**: We’ll keep the filter text and checked state values in `FilterableProductTable`.

So the state values will live in `FilterableProductTable`.

### 6. Add inverse data flow
- To change the state according to user input, you will need to support data flowing the other way: the form components deep in the hierarchy need to update the state in FilterableProductTable
- To change the state in a child component, you will need to send the function that you declared in the setState into the component itself.
- 

## Concepts

#### Props Vs State
There are two types of “model” data in React: props and state. The two are very different:

- [**Props** are like arguments you pass](https://react.dev/learn/passing-props-to-a-component) to a function. They let a parent component pass data to a child component and customize its appearance. For example, a `Form` can pass a `color` prop to a `Button`.
- [**State** is like a component’s memory.](https://react.dev/learn/state-a-components-memory) It lets a component keep track of some information and change it in response to interactions. For example, a `Button` might keep track of `isHovered` state.

Props and state are different, but they work together. A parent component will often keep some information in state (so that it can change it), and _pass it down_ to child components as their props. It’s okay if the difference still feels fuzzy on the first read. It takes a bit of practice for it to really stick!
### Resources
https://react.dev/learn/thinking-in-react

Routing Libraries
ReactRouter - https://reactrouter.com/en/main
Vike - https://vike.dev/