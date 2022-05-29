import React from 'react';
import axios from 'axios';
//import logo from './logo.svg';
import './App.css';
import UsersList from './components/user.js'

class App extends React.Component{
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/user')
      .then(response => {
        const users = response.data
          this.setState(
          {
          'users': users
          }
          )
      }).catch(error => console.log(error))

    /*const user = [
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
    */
  }

  render () {
    return (
      <div>
        <UsersList users={this.state.users} />
      </div>
    )
  }
}

export default App;
