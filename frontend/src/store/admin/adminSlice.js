import { createSlice } from '@reduxjs/toolkit'
import { initialState } from './initialState'

const adminSlice = createSlice({
  name: 'admin',
  initialState: initialState,
  reducers: {
    handleClickOrders: state => {
      state.linkView = 'orders'
    },
    handleClickServices: state => {
      state.linkView = 'services'
    },
    handleClickStaff: state => {
      state.linkView = 'staff'
    },
    handleClickStatistics: state => {
      state.linkView = 'statistics'
    },
    handleClickNew: state => {
      state.tab = 'new'
    },
    handleClickCurrent: state => {
      state.tab = 'current'
    },
    handleClickCompleted: state => {
      state.tab = 'completed'
    },
    handleClickСancelled: state => {
      state.tab = 'cancelled'
    },
  },
})

export const {
  handleClickOrders,
  handleClickServices,
  handleClickStaff,
  handleClickStatistics,
  handleClickNew,
  handleClickCurrent,
  handleClickCompleted,
  handleClickСancelled,
} = adminSlice.actions
export default adminSlice.reducer