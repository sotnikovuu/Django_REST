import React from 'react';
// import axios from 'axios';
// import logo from './logo.svg';
import './App.css';
import UserList from './components/user.js'

class App extends React.Component{
  constructor(props) {
    super(props)
    this.state = {
      'user': []
    }
  }

  componentDidMount() {
    const user = [
      {
        'username': 'sotnik',
        'firstname': 'Юрий',
        'lastname': 'Сотников',
        'email': 'sotnik@test.ru'
      },
      {
        'username': 'test',
        'firstname': 'Тестовый',
        'lastname': 'Тестировщик',
        'email': 'test@test.ru'
      },
    ]
    this.setState(
      {
        'user': user
      }
    )
  }

  render () {
    return (
      <div>
        <UserList user={this.state.user} />
      </div>
    )
  }
}

export default App;
